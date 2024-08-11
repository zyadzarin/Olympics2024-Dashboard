import React, { useState, useEffect, useRef } from 'react';
import { Chart } from 'chart.js/auto';
import { ChoroplethController, ProjectionScale, ColorScale, GeoFeature } from 'chartjs-chart-geo';

import { feature } from 'topojson-client';
import axios from '../../api';
Chart.register(ChoroplethController, ProjectionScale, ColorScale, GeoFeature);

const WorldMap = () => {
  const [selectedCountry, setSelectedCountry] = useState(null);
  const [countries, setCountries] = useState([]);
  const [medalData, setMedalData] = useState([]);
  const chartRef = useRef(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [topojsonResponse, medalResponse] = await Promise.all([
          fetch('https://unpkg.com/world-atlas@2.0.2/countries-50m.json'),
          axios.get('/country_medals/') // Adjust this endpoint to match your API
        ]);

        const topojsonData = await topojsonResponse.json();
        const countries = feature(topojsonData, topojsonData.objects.countries);
        setCountries(countries);

        setMedalData(medalResponse.data);
        console.log(medalResponse.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    if (!countries.features || medalData.length === 0) return;
    const ctx = chartRef.current.getContext('2d');
    const chart = new Chart(ctx, {
      type: 'choropleth',
      data: {
        labels: countries.features.map((d) => d.properties.name),
        datasets: [{
          label: 'Countries',
          data: countries.features.map((d) => (            {
            feature: d,
            value: medalData.find(c => c.country_full === d.properties.name)?.total || 0
          })),
        }]
      },
      options: {
        showOutline: true,
        showGraticule: true,
        plugins: {
          legend: {
            display: false
          },
          datalabels: {
            display: false
          }
        },
        scales: {
          projection: {
            axis: 'x',
            projection: 'equalEarth'
          },
          color: {
            axis: 'x',
            quantize: 5,
            legend: {
              position: 'bottom-right',
              align: 'bottom',
              title: {
                display: true,
                text: 'Total Medals'
              }
            },
          }
        },
        onClick: (e, elements) => {
          if (elements.length > 0) {
            const countryName = elements[0].element.feature.properties.name;
            const country = medalData.find(c => c.country_full === countryName);
            setSelectedCountry(country);
          }
        }
      }
    });

    return () => {
      chart.destroy();
    };
  }, [countries, medalData]);

  return (
    <div className="container px-4 py-8">
      <h1 className="text-3xl font-bold mb-6 text-center">Olympic Medal Dashboard</h1>
      <div className="mb-8 ">
        <canvas ref={chartRef}></canvas>
      </div>
      {selectedCountry && (
        <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <h2 className="text-2xl font-semibold ">{selectedCountry.country} Details</h2>
          <table className="w-full table-auto">
            <thead>
              <tr className="bg-gray-200">
                <th className="px-4 py-2 text-left">Medal Type</th>
                <th className="px-4 py-2 text-left">Count</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="border px-4 py-2">Gold</td>
                <td className="border px-4 py-2">{selectedCountry.gold}</td>
              </tr>
              <tr>
                <td className="border px-4 py-2">Silver</td>
                <td className="border px-4 py-2">{selectedCountry.silver}</td>
              </tr>
              <tr>
                <td className="border px-4 py-2">Bronze</td>
                <td className="border px-4 py-2">{selectedCountry.bronze}</td>
              </tr>
              <tr className="font-semibold">
                <td className="border px-4 py-2">Total</td>
                <td className="border px-4 py-2">{selectedCountry.total}</td>
              </tr>
              <tr>
                <td className="border px-4 py-2">Number of Athletes</td>
                <td className="border px-4 py-2">{selectedCountry.athletes_num}</td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default WorldMap;