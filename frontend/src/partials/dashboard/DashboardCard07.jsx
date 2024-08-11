import React, { useState, useEffect } from 'react';
import AgeDistributionOfMedalists from '../../charts/AgeDistributionOfMedalists';

// Dummy data generator (slightly modified to ensure a wider age range)
const generateDummyData = (count) => {
  const countries = ['USA', 'CHN', 'JPN', 'GBR', 'RUS', 'AUS', 'ITA', 'FRA', 'GER', 'CAN'];
  const events = ['Swimming', 'Athletics', 'Gymnastics', 'Cycling', 'Rowing', 'Tennis', 'Basketball', 'Volleyball'];
  
  return Array.from({ length: count }, (_, i) => ({
    name: `Athlete ${i + 1}`,
    gender: Math.random() > 0.5 ? 'Male' : 'Female',
    nationality: countries[Math.floor(Math.random() * countries.length)],
    country_code: countries[Math.floor(Math.random() * countries.length)],
    event: events[Math.floor(Math.random() * events.length)],
    age: Math.floor(Math.random() * 30) + 15, // Ages from 15 to 44
    gold: Math.floor(Math.random() * 3),
    silver: Math.floor(Math.random() * 3),
    bronze: Math.floor(Math.random() * 3),
  }));
};

function DashboardCard07() {
  const [athletesData, setAthletesData] = useState([]);

  useEffect(() => {
    // Simulating API call with dummy data
    const dummyData = generateDummyData(1000);
    setAthletesData(dummyData);
  }, []);

  return (
    <div className="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Age Distribution of Olympic Medalists</h2>
      </div>
      <div className="flex-grow p-4">
        <AgeDistributionOfMedalists athletesData={athletesData} />
      </div>
    </div>
  );
}

export default DashboardCard07;