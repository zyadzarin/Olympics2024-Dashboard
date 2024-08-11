import React, { useState, useEffect } from 'react';
import AgeDistributionOfMedalists from '../../charts/AgeDistributionOfMedalists';
import axios from '../../api';

function DashboardCard07() {
  const [athletesData, setAthletesData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);
        const response = await axios.get('top_medallists/'); // Adjust the endpoint as needed
        setAthletesData(response.data);
        setIsLoading(false);
      } catch (err) {
        setError('Failed to fetch data');
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Age Distribution of Top 100 Olympic Medalists</h2>
      </div>
      <div className="flex-grow p-4">
        {isLoading ? (
          <p>Loading...</p>
        ) : error ? (
          <p className="text-red-500">{error}</p>
        ) : (
          <AgeDistributionOfMedalists athletesData={athletesData} />
        )}
      </div>
    </div>
  );
}

export default DashboardCard07;