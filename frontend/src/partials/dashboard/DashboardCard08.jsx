import React, { useState, useEffect } from 'react';
import axios from '../../api';
import TopCountriesMedalChart from '../../charts/TopCountriesMedalChart';

function DashboardCard08() {
  const [medalData, setMedalData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);
        // Assuming the endpoint is configured in the axios instance
        const response = await axios.get('top_countries_athletes/');
        setMedalData(response.data);
      } catch (error) {
        setError(error.response?.data?.message || 'An error occurred while fetching data');
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  if (isLoading) {
    return (
      <div className="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl p-5">
        <div className="text-center">Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl p-5">
        <div className="text-center text-red-500">Error: {error}</div>
      </div>
    );
  }

  return (
    <div className="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Top Countries Medal Distribution</h2>
      </div>
      <div className="flex-grow p-4">
        {medalData && <TopCountriesMedalChart data={medalData} />}
      </div>
    </div>
  );
}

export default DashboardCard08;