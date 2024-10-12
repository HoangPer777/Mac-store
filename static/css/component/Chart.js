const viewData = [
    234, 294, 190, 253, 239, 219,
    190, 183, 189, 139, 153, 185,
    190, 201, 195, 198, 167, 125,
    184, 213, 201, 213, 250, 187,
    163, 212, 163, 143, 210, 280
];

// Tạo dữ liệu biến động cho Designer Edition với cùng biến động, nhưng giao thoa với Developer Edition
const purchasesData = [
    30, 49, 35,46 , 35, 30,
    41, 43, 45, 32, 50, 45,
    49, 32, 36, 38, 49, 32,
    30, 44, 32, 33, 49, 33,
    44, 33, 46, 32, 39, 50
];
const options = {
    grid: {
        show: true,
        strokeDashArray: 4,
        padding: {
            left: 2,
            right: 2,
            top: -26,
        },
    },
    series: [
        {
            name: "Views",
            data: viewData,
            color: "#1A56DB",
        },
        {
            name: "Purchases",
            data: purchasesData,
            color: "#7E3BF2",
        },
    ],
    chart: {
        height: 300,
        width: 1100,
        type: "area",
        fontFamily: "Inter, sans-serif",
        dropShadow: {
            enabled: false,
        },
        toolbar: {
            show: false,
        },
    },
    tooltip: {
        enabled: true,
        x: {
            show: false,
        },
    },
    legend: {
        show: true,
    },
    fill: {
        type: "gradient",
        gradient: {
            opacityFrom: 0.55,
            opacityTo: 0,
            shade: "#1C64F2",
            gradientToColors: ["#1C64F2"],
        },
    },
    dataLabels: {
        enabled: false,
    },
    stroke: {
        width: 6,
    },
    xaxis: {
        categories: Array.from({ length: 30 }, (_, i) => ` ${i + 1}`),
        labels: {
            show: true,
        },
        axisBorder: {
            show: false,
        },
        axisTicks: {
            show: false,
        },
    },
    yaxis: {
        show: false,
        labels: {
            formatter: function (value) {
                return ' ' + value;
            },
        },
    },
};

// Kiểm tra nếu ApexCharts đã được tải và có thẻ chứa biểu đồ
if (document.getElementById("grid-chart") && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(document.getElementById("grid-chart"), options);
    chart.render();
}




