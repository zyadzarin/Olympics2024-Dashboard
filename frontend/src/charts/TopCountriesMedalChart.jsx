import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

const TopCountriesMedalChart = ({ data }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (chartInstance.current) {
      chartInstance.current.destroy();
    }

    const ctx = chartRef.current.getContext('2d');

    chartInstance.current = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.top_countries.map(country => country.country_code),
        datasets: [
          {
            label: 'Gold Medals',
            data: data.top_countries.map(country => country.gold_medal),
            backgroundColor: 'gold',
          },
          {
            label: 'Silver Medals',
            data: data.top_countries.map(country => country.silver_medal),
            backgroundColor: 'silver',
          },
          {
            label: 'Bronze Medals',
            data: data.top_countries.map(country => country.bronze_medal),
            backgroundColor: '#CD7F32',
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Medal Distribution for Top Countries',
          },
          tooltip: {
            callbacks: {
              afterBody: (tooltipItems) => {
                const countryData = data.top_countries[tooltipItems[0].dataIndex];
                return `Total Medals: ${countryData.total}\nTop Athletes:\n${countryData.athletes.map(athlete => `${athlete.name}: ${athlete.medals.length} medal(s)`).join('\n')}`;
              },
            },
          },
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Countries',
            },
          },
          y: {
            title: {
              display: true,
              text: 'Number of Medals',
            },
            beginAtZero: true,
          },
        },
      },
    });

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [data]);

  return <canvas ref={chartRef} />;
};

export default TopCountriesMedalChart;