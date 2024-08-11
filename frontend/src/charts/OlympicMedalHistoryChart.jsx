import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';

const OlympicMedalHistoryChart = ({ data, width, height }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  // List of Winter Olympic years
  const winterOlympicYears = [
    1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022
  ];

  useEffect(() => {
    const createOrUpdateChart = () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }

      if (chartRef.current && data && data.medals_history) {
        const ctx = chartRef.current.getContext('2d');
        
        const summerData = data.medals_history
        const winterData = data.medals_history.filter(d => winterOlympicYears.includes(parseInt(d.year)));

        const createDataset = (label, data, color, dashStyle) => ({
          label,
          data: data.map(d => ({ 
            x: parseInt(d.year), 
            y: parseInt(d[label.split(' ')[0].toLowerCase()]) 
          })),
          borderColor: color,
          backgroundColor: color,
          borderDash: dashStyle,
          fill: false,
          pointRadius: 3,
          tension: 0.1
        });

        const datasets = [
          createDataset('Gold (Summer)', summerData, 'gold', []),
          createDataset('Silver (Summer)', summerData, 'silver', []),
          createDataset('Bronze (Summer)', summerData, '#CD7F32', []),
          createDataset('Total (Summer)', summerData, 'red', []),
          // createDataset('Gold (Winter)', winterData, 'rgba(255, 215, 0, 0.5)', [5, 5]),
          // createDataset('Silver (Winter)', winterData, 'rgba(192, 192, 192, 0.5)', [5, 5]),
          // createDataset('Bronze (Winter)', winterData, 'rgba(205, 127, 50, 0.5)', [5, 5]),
          // createDataset('Total (Winter)', winterData, 'rgba(255, 0, 0, 0.5)', [5, 5]),
        ];

        console.log('Datasets:', datasets); // Debug log

        chartInstance.current = new Chart(ctx, {
          type: 'line',
          data: { datasets },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              x: {
                type: 'linear',
                title: {
                  display: true,
                  text: 'Year'
                },
                ticks: {
                  stepSize: 4
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'Number of Medals'
                },
                beginAtZero: true
              }
            },
            plugins: {
              title: {
                display: true,
                text: `${data.country} - Olympic Medal History`
              },
              legend: {
                position: 'top',
                labels: {
                  usePointStyle: true,
                  pointStyle: 'circle',
                  boxWidth: 8
                }
              },
              tooltip: {
                mode: 'index',
                intersect: false
              }
            },
            interaction: {
              mode: 'nearest',
              axis: 'x',
              intersect: false
            }
          }
        });
      }
    };

    createOrUpdateChart();

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [data]);

  return <canvas ref={chartRef} width={width} height={height} />;
};

export default OlympicMedalHistoryChart;