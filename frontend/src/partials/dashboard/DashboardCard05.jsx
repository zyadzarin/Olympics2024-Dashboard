import React, { useState, useEffect } from 'react';
import axios from '../../api';
import OlympicMedalHistoryChart from '../../charts/OlympicMedalHistoryChart';

function DashboardCard05() {
  const [countries, setCountries] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState('USA');
  const [medalHistory, setMedalHistory] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch list of countries
    const fetchCountries = async () => {
      try {
        const response = await axios.get('country_info/');
        setCountries(response.data);
        
        // Check if USA is in the list, if not, select the first country
        const usaExists = response.data.some(country => country.country_code === 'USA');
        if (!usaExists && response.data.length > 0) {
          setSelectedCountry(response.data[0].country_code);
        }
      } catch (err) {
        setError('Failed to fetch countries');
      }
    };

    fetchCountries();
  }, []);

  useEffect(() => {
    // Fetch medal history for selected country
    const fetchMedalHistory = async () => {
      if (!selectedCountry) return;

      setIsLoading(true);
      setError(null);

      try {
        const response = await axios.get(`country_medals_history/?country_code=${selectedCountry}`);
        setMedalHistory(response.data[0]);
        console.log(response.data);
        setIsLoading(false);
      } catch (err) {
        setError('Failed to fetch medal history');
        setIsLoading(false);
      }
    };

    fetchMedalHistory();
  }, [selectedCountry]);

  return (
    <div className="flex flex-col col-span-full xl:col-span-12 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Olympic Medal History</h2>
        <div className="flex space-x-2 mb-4">
          <select 
            value={selectedCountry} 
            onChange={(e) => setSelectedCountry(e.target.value)}
            className="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          >
            {countries.map((country) => (
              <option key={country.country_code} value={country.country_code}>
                {country.country}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div className="flex-grow px-5 pb-5">
        {isLoading ? (
          <p>Loading...</p>
        ) : error ? (
          <p className="text-red-500">{error}</p>
        ) : medalHistory ? (
          <OlympicMedalHistoryChart 
            data={medalHistory} 
            width={1000} 
            height={600} 
          />
        ) : null}
      </div>
    </div>
  );
}

export default DashboardCard05;