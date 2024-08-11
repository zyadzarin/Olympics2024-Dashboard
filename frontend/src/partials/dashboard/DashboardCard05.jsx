import React, { useState } from 'react';
import OlympicMedalHistoryChart from '../../charts/OlympicMedalHistoryChart';

// Dummy data (expanded to include both summer and winter years)
const dummyData = {
  "USA": {
    "country": "United States of America",
    "country_code": "USA",
    "medals_history": [
      { "Year": "1896", "Bronze": 30, "Silver": 34, "Gold": 23, "Total": 87 },
      { "Year": "1898", "Bronze": 15, "Silver": 17, "Gold": 12, "Total": 44 },
      { "Year": "1900", "Bronze": 32, "Silver": 36, "Gold": 25, "Total": 93 },
      { "Year": "1902", "Bronze": 16, "Silver": 18, "Gold": 13, "Total": 47 },
      { "Year": "1904", "Bronze": 34, "Silver": 38, "Gold": 27, "Total": 99 },
      // ... add more years here
      { "Year": "2020", "Bronze": 33, "Silver": 41, "Gold": 39, "Total": 113 },
      { "Year": "2022", "Bronze": 17, "Silver": 20, "Gold": 19, "Total": 56 },
      { "Year": "2024", "Bronze": 30, "Silver": 34, "Gold": 27, "Total": 91 }
    ]
  },
  "GBR": {
    "country": "United Kingdom",
    "country_code": "GBR",
    "medals_history": [
      { "Year": "1896", "Bronze": 20, "Silver": 24, "Gold": 13, "Total": 57 },
      { "Year": "1898", "Bronze": 10, "Silver": 12, "Gold": 7, "Total": 29 },
      { "Year": "1900", "Bronze": 22, "Silver": 26, "Gold": 15, "Total": 63 },
      { "Year": "1902", "Bronze": 11, "Silver": 13, "Gold": 8, "Total": 32 },
      { "Year": "1904", "Bronze": 24, "Silver": 28, "Gold": 17, "Total": 69 },
      // ... add more years here
      { "Year": "2020", "Bronze": 23, "Silver": 31, "Gold": 29, "Total": 83 },
      { "Year": "2022", "Bronze": 12, "Silver": 15, "Gold": 14, "Total": 41 },
      { "Year": "2024", "Bronze": 20, "Silver": 24, "Gold": 17, "Total": 61 }
    ]
  }
  // Add more countries here
};

function DashboardCard05() {
  const [selectedCountry, setSelectedCountry] = useState('USA');

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
            {Object.keys(dummyData).map((countryCode) => (
              <option key={countryCode} value={countryCode}>
                {dummyData[countryCode].country}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div className="flex-grow px-5 pb-5">
        <OlympicMedalHistoryChart 
          data={dummyData[selectedCountry]} 
          width={1000} 
          height={600} 
        />
      </div>
    </div>
  );
}

export default DashboardCard05;