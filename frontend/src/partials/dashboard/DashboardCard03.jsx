import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import EditMenu from '../../components/DropdownEditMenu';
import SimpleBarChart from '../../charts/SimpleBarChart';
import axios from '../../api/index';

function DashboardCard03() {
  const [sportsData, setSportsData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('sports/');
        const sortedSports = response.data.sports
          .sort((a, b) => b.total_medals - a.total_medals)
          .slice(0, 10);
        setSportsData(sortedSports);
      } catch (error) {
        console.error('Error fetching sports data:', error);
      }
    };

    fetchData();
  }, []);

  const chartData = sportsData.length > 0 ? {
    labels: sportsData.map(sport => sport.sport),
    datasets: [
      {
        label: 'Total Medals',
        data: sportsData.map(sport => sport.total_medals),
      }
    ]
  } : null;

  return (
    <div className="flex flex-col col-span-full sm:col-span-6 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <header className="flex justify-between items-start mb-2">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Top 10 Sports by Medals</h2>
        </header>
      </div>
      <div className="flex-grow">
        {chartData ? (
          <SimpleBarChart data={chartData} width={595} height={248} />
        ) : (
          <div className="flex items-center justify-center h-full">Loading...</div>
        )}
      </div>
    </div>
  );
}

export default DashboardCard03;