import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';

const TopAthletesChart = ({ data, width, height }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    const createOrUpdateChart = () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }

      if (chartRef.current && data && data.length > 0) {
        const ctx = chartRef.current.getContext('2d');

        // Sort athletes by total medals and get top 10
        const topAthletes = data
          .sort((a, b) => (b.gold + b.silver + b.bronze) - (a.gold + a.silver + a.bronze))
          .slice(0, 10);

        chartInstance.current = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: topAthletes.map(athlete => athlete.name),
            datasets: [
              {
                label: 'Gold',
                data: topAthletes.map(athlete => athlete.gold),
                backgroundColor: 'gold',
              },
              {
                label: 'Silver',
                data: topAthletes.map(athlete => athlete.silver),
                backgroundColor: 'silver',
              },
              {
                label: 'Bronze',
                data: topAthletes.map(athlete => athlete.bronze),
                backgroundColor: '#CD7F32',
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              x: {
                stacked: true,
                title: {
                  display: true,
                  text: 'Athletes',
                },
              },
              y: {
                stacked: true,
                title: {
                  display: true,
                  text: 'Number of Medals',
                },
                beginAtZero: true,
              },
            },
            plugins: {
              title: {
                display: true,
                text: 'Top 10 Athletes by Medal Count',
              },
              tooltip: {
                mode: 'index',
                intersect: false,
              },
            },
          },
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

export default TopAthletesChart;