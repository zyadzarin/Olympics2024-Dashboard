import React, { useState, useEffect } from 'react';
import axios from '../api';

const OlympicMedalDisplay = () => {
  const [sports, setSports] = useState([]);
  const [countries, setCountries] = useState([]);
  const [athletes, setAthletes] = useState([]);
  const [selectedSport, setSelectedSport] = useState('');
  const [selectedCountry, setSelectedCountry] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('top_countries_athletes/');
        const data = response.data;
        
        // Extract unique sports and countries
        const uniqueSports = [...new Set(data.map(athlete => athlete.sport))];
        const uniqueCountries = [...new Set(data.map(athlete => athlete.country))];
        
        setSports(uniqueSports.sort());
        setCountries(uniqueCountries.sort());
        setAthletes(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const filteredAthletes = athletes.filter(athlete => {
    if (selectedSport && selectedCountry) {
      return athlete.sport === selectedSport && athlete.country === selectedCountry;
    } else if (selectedSport) {
      return athlete.sport === selectedSport;
    } else if (selectedCountry) {
      return athlete.country === selectedCountry;
    }
    return true;
  });

  const sortedAthletes = filteredAthletes.sort((a, b) => {
    const medalOrder = { 'Gold': 3, 'Silver': 2, 'Bronze': 1, 'No Medal': 0 };
    return medalOrder[b.medal] - medalOrder[a.medal];
  });

  const renderAthletes = () => {
    if (sortedAthletes.length === 0) {
      return <p>No athletes found for the selected criteria.</p>;
    }

    return (
      <ul className="space-y-2">
        {sortedAthletes.map((athlete, index) => (
          <li key={index} className="border-b pb-2">
            {athlete.medal !== 'No Medal' ? (
              <span className="font-bold">
                {athlete.medal}: {athlete.name} 
              </span>
            ) : (
              <span>{athlete.name}</span>
            )}
            {(!selectedCountry || selectedSport) && (
              <span className="ml-2 text-gray-600">({athlete.country})</span>
            )}
            {(!selectedSport || selectedCountry) && (
              <span className="ml-2 text-gray-600">{athlete.sport}</span>
            )}
          </li>
        ))}
      </ul>
    );
  };

  return (
    <div className="flex flex-col col-span-full xl:col-span-12 bg-white dark:bg-gray-800 shadow-sm rounded-xl p-4">
      <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-4">Olympic Athletes</h2>
      <div className="flex space-x-4 mb-4">
        <select
          value={selectedSport}
          onChange={(e) => setSelectedSport(e.target.value)}
          className="w-1/2 p-2 border rounded dark:bg-gray-700 dark:text-white"
        >
          <option value="">Select a sport</option>
          {sports.map((sport, index) => (
            <option key={index} value={sport}>{sport}</option>
          ))}
        </select>
        <select
          value={selectedCountry}
          onChange={(e) => setSelectedCountry(e.target.value)}
          className="w-1/2 p-2 border rounded dark:bg-gray-700 dark:text-white"
        >
          <option value="">Select a country</option>
          {countries.map((country, index) => (
            <option key={index} value={country}>{country}</option>
          ))}
        </select>
      </div>
      <div className="mt-4">
        {renderAthletes()}
      </div>
    </div>
  );
};

export default OlympicMedalDisplay;