document.addEventListener("DOMContentLoaded", function () {
  initGaugeChart();
  initFeatureComparison();
  initCustomerCluster();
  initTimeTrend();
});

function initGaugeChart() {
  const chart = echarts.init(document.querySelector("#gauge .chart-container"));
  chart.setOption({
    series: [
      {
        type: "gauge",
        detail: {
          formatter: "{value}%",
          fontSize: 20,
          color: "#ff0000",
        },
        data: [{ value: 72.4, name: "续保率" }],
        pointer: {
          show: true,
          length: "80%",
          width: 8,
        },
        animation: true,
        animationDuration: 2000,
      },
    ],
  });
}

function initFeatureComparison() {
  const chart = echarts.init(
    document.querySelector("#feature-comparison .chart-container")
  );
  chart.setOption({
    radar: {
      indicator: ["年龄", "婚姻状态", "家庭人数", "保单日期"],
      splitArea: {
        show: false,
      },
      axisLine: {
        lineStyle: {
          color: "rgba(0, 0, 0, 0.3)",
        },
      },
    },
    series: [
      {
        type: "radar",
        lineStyle: {
          width: 4,
        },
        symbolSize: 12,
        areaStyle: {
          opacity: 0.5,
        },
        label: {
          show: true,
          formatter: function (params) {
            return params.value.toFixed(2);
          },
          fontSize: 12,
          fontWeight: "bold",
        },
        data: [
          {
            value: [0.85, 0.72, 0.68, 0.63],
            name: "逻辑回归",
            lineStyle: { width: 4 },
          },
          {
            value: [0.91, 0.82, 0.75, 0.58],
            name: "决策树",
            lineStyle: { width: 4 },
          },
        ],
      },
    ],
  });
}

function initTimeTrend() {
  const chart = echarts.init(
    document.querySelector("#time-trend .chart-container")
  );
  chart.setOption({
    xAxis: {
      type: "category",
      data: ["2023Q1", "2023Q2", "2023Q3", "2023Q4"],
      axisLine: {
        lineStyle: {
          color: "#666",
        },
      },
    },
    yAxis: {
      type: "value",
      axisLine: {
        lineStyle: {
          color: "#666",
        },
      },
    },
    series: [
      {
        data: [68, 71, 75, 72],
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 10,
        itemStyle: {
          color: "#c23531",
        },
        lineStyle: {
          width: 3,
        },
        label: {
          show: true,
          formatter: "{c}%",
          position: "top",
        },
      },
    ],
  });
}

function initCustomerCluster() {
  const chart = echarts.init(
    document.querySelector("#customer-cluster .chart-container")
  );
  chart.setOption({
    series: [
      {
        type: "pie",
        radius: ["40%", "70%"],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: "#fff",
          borderWidth: 2,
        },
        label: {
          show: true,
          formatter: "{b}: {d}%",
        },
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)",
          },
        },
        data: [
          { value: 35, name: "高价值客户", itemStyle: { color: "#2f4554" } },
          { value: 45, name: "普通客户", itemStyle: { color: "#61a0a8" } },
          { value: 20, name: "风险客户", itemStyle: { color: "#c23531" } },
        ],
      },
    ],
  });
}
