import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import EditMenu from '../../components/DropdownEditMenu';
import SimpleDoughnutChart from '../../charts/SimpleDoughnutChart';
import axios from '../../api/index';

function DashboardCard04() {
  const [sportsData, setSportsData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/sports');
        const sortedSports = response.data.sports
          .sort((a, b) => b.total_participants - a.total_participants)
          .slice(0, 5);
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
        data: sportsData.map(sport => sport.total_participants),
      }
    ]
  } : null;

  return (
    <div className="flex flex-col col-span-full sm:col-span-6 xl:col-span-3 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <header className="flex justify-between items-start mb-2">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Top 5 Sports by Participation</h2>
        </header>
      </div>
      <div className="flex-grow flex items-center justify-center">
        {chartData ? (
          <SimpleDoughnutChart data={chartData} width={389} height={260} />
        ) : (
          <div>Loading...</div>
        )}
      </div>
    </div>
  );
}

export default DashboardCard04;