from django.shortcuts import render

import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Feedback
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.utils import timezone

from django.http import JsonResponse


# Nạp mô hình và vectorizer
MODEL_PATH = 'feed_back/model/random_forest_model.pkl'
VECTORIZER_PATH = 'feed_back/model/vectorizer.pkl'

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@csrf_exempt
def save_feedback(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        product_id = request.POST.get('product_id')
        rating = int(request.POST.get('rating', 5))
        comment = request.POST.get('comment', '')

        if not user_id or not comment or not product_id:
            return JsonResponse({'error': 'User ID, Product ID, and comment are required'}, status=400)

        # Sử dụng foreign key đúng
        feedback = Feedback.objects.create(
            userID_id=user_id,
            productID_id=product_id,
            rating=rating,
            comment=comment,
            type=None  # Chưa phân loại
        )

        return JsonResponse({'message': 'Lưu bình luận thành công', 'id': feedback.id})

    return JsonResponse({'error': 'Invalid request method'}, status=405)




@csrf_exempt
def classify_feedback(request):
    if request.method == 'POST':
        # Lấy tất cả các feedback chưa phân loại
        pending_feedbacks = Feedback.objects.filter(type__isnull=True)

        if not pending_feedbacks.exists():
            return JsonResponse({'message': 'Không có bình luận nào đang chờ phân loại'})

        classified_feedbacks = []  # Danh sách các feedback đã được phân loại

        for feedback in pending_feedbacks:
            comment_vectorized = vectorizer.transform([feedback.comment])
            prediction = model.predict(comment_vectorized)
            feedback.type = 1 if prediction[0] == 'toxic' else 0
            feedback.save()

            classified_feedbacks.append({
                'id': feedback.id,
                'comment': feedback.comment,
                'type': 'toxic' if feedback.type == 1 else 'normal'
            })

        return JsonResponse({
            'message': 'Phân loại thành công',
            'classified_count': pending_feedbacks.count(),
            'classified_feedbacks': classified_feedbacks
        })

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_feedback(request):
    if request.method == 'POST':
        try:
            # Get the feedback IDs from the request
            data = json.loads(request.body)
            feedback_ids = data.get('feedback_ids', [])

            if not feedback_ids:
                return JsonResponse({'error': 'No feedback IDs provided'}, status=400)

            # Delete the feedbacks from the database
            Feedback.objects.filter(id__in=feedback_ids).delete()

            return JsonResponse({'message': 'Đã xóa những bình luận được chọn'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)