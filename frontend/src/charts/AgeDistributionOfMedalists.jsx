import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import 'chartjs-plugin-datalabels';

const AgeDistributionOfMedalists = ({ athletesData }) => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    // Filter athletes who won at least one medal
    const medalists = athletesData.filter(athlete => athlete.gold + athlete.silver + athlete.bronze > 0);

    // Create age distribution
    const ageDistribution = medalists.reduce((acc, athlete) => {
      acc[athlete.age] = (acc[athlete.age] || 0) + 1;
      return acc;
    }, {});

    // Find min and max ages
    const minAge = Math.min(...Object.keys(ageDistribution).map(Number));
    const maxAge = Math.max(...Object.keys(ageDistribution).map(Number));

    // Create an array for all ages, including those with zero medalists
    const allAges = Array.from({ length: maxAge - minAge + 1 }, (_, i) => i + minAge);
    const medalCounts = allAges.map(age => ageDistribution[age] || 0);

    setChartData({
      labels: allAges,
      datasets: [
        {
          label: 'Number of Medalists',
          data: medalCounts,
          backgroundColor: 'rgba(75, 192, 192, 0.6)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 0,
          barPercentage: 1.0,
          categoryPercentage: 1.0,
        },
      ],
    });
  }, [athletesData]);

  if (!chartData) return <div>Loading...</div>;

  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Age Distribution of 2024 Olympic Medalists',
        font: {
          size: 16,
        },
      },
      datalabels: {
        display: false, // Hide data labels to prevent clutter
      },
      tooltip: {
        callbacks: {
          title: (tooltipItems) => `Age: ${tooltipItems[0].label}`,
          label: (context) => `Medalists: ${context.parsed.y}`,
        },
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Age',
        },
        
      },
      y: {
        title: {
          display: true,
          text: 'Number of Medalists',
        },
        beginAtZero: true,
      },
    },
  };

  return <Bar data={chartData} options={options} />;
};

export default AgeDistributionOfMedalists;