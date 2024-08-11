import React, { useState, useEffect } from 'react';
import TopAthletesChart from '../../charts/TopAthletesChart';

// Dummy data generator
const generateDummyData = (count) => {
  const countries = ['USA', 'CHN', 'JPN', 'GBR', 'RUS', 'AUS', 'ITA', 'FRA', 'GER', 'CAN'];
  const events = ['Swimming', 'Athletics', 'Gymnastics', 'Cycling', 'Rowing', 'Tennis', 'Basketball', 'Volleyball'];
  
  return Array.from({ length: count }, (_, i) => ({
    name: `Athlete ${i + 1}`,
    gender: Math.random() > 0.5 ? 'Male' : 'Female',
    nationality: countries[Math.floor(Math.random() * countries.length)],
    country_code: countries[Math.floor(Math.random() * countries.length)],
    event: events[Math.floor(Math.random() * events.length)],
    age: Math.floor(Math.random() * 20) + 15,
    gold: Math.floor(Math.random() * 5),
    silver: Math.floor(Math.random() * 5),
    bronze: Math.floor(Math.random() * 5),
  }));
};

function DashboardCard06() {
  const [athletesData, setAthletesData] = useState([]);

  useEffect(() => {
    // Simulating API call with dummy data
    const dummyData = generateDummyData(50);
    setAthletesData(dummyData);
  }, []);

  return (
    <div className="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Top 10 Athletes by Medal Count</h2>
      </div>
      <div className="flex-grow">
        <TopAthletesChart data={athletesData} width={800} height={400} />
      </div>
    </div>
  );
}

export default DashboardCard06;