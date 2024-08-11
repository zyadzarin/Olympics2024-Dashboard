import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';
import ChartDataLabels from 'chartjs-plugin-datalabels';

const SimpleBarChart = ({ data, width, height }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  
  useEffect(() => {
    // Function to create or update the chart
    const createOrUpdateChart = () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
      
      if (chartRef.current && data && data.labels && data.datasets) {
        const ctx = chartRef.current.getContext('2d');
        chartInstance.current = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: data.labels,
            datasets: [{
              label: 'Total Medals',
              data: data.datasets[0].data,
              backgroundColor: 'rgba(99, 102, 241, 0.8)',
              borderColor: 'rgba(99, 102, 241, 1)',
              borderWidth: 1
            }]
          },
          plugins: [ChartDataLabels],
          options: {
            indexAxis: 'y',
            responsive: true,
            
            maintainAspectRatio: false,
            scales: {
              x: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Number of Medals'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'Sports'
                }
              }
            },
            plugins: {
                
              legend: {
                display: false
              },
              tooltip: {
                enabled: false
             },
             datalabels:{
                display: true,
                color: 'black',

             }
            },

          }
        })
        ;
      }
      
    };

    createOrUpdateChart();

    // Cleanup function
    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [data]);

  return <canvas ref={chartRef} width={width} height={height} />;
};

export default SimpleBarChart;