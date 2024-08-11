import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
import { Chart } from 'chart.js/auto';
import { ChoroplethController, ProjectionScale, ColorScale, GeoFeature } from 'chartjs-chart-geo';
import { feature } from 'topojson-client';
import EditMenu from '../../components/DropdownEditMenu';
import axios from '../../api';

Chart.register(ChoroplethController, ProjectionScale, ColorScale, GeoFeature);

function DashboardCard02() {
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
          data: countries.features.map((d) => ({
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
    <div className="flex flex-col col-span-full xl:col-span-12 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <div className="px-5 pt-5">
        <header className="flex justify-between items-start mb-2">
          <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Olympic Medal Map</h2>
          <EditMenu align="right" className="relative inline-flex">
            <li>
              <Link className="font-medium text-sm text-gray-600 dark:text-gray-300 hover:text-gray-800 dark:hover:text-gray-200 flex py-1 px-3" to="#0">
                Option 1
              </Link>
            </li>
            <li>
              <Link className="font-medium text-sm text-gray-600 dark:text-gray-300 hover:text-gray-800 dark:hover:text-gray-200 flex py-1 px-3" to="#0">
                Option 2
              </Link>
            </li>
            <li>
              <Link className="font-medium text-sm text-red-500 hover:text-red-600 flex py-1 px-3" to="#0">
                Remove
              </Link>
            </li>
          </EditMenu>
        </header>
      </div>
      <div className="grow">
        <canvas ref={chartRef} className="w-full h-[400px]"></canvas>
      </div>
      {selectedCountry && (
        <div className="px-5 py-3 border-t border-gray-200 dark:border-gray-700">
          <h3 className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase mb-1">{selectedCountry.country} Details</h3>
          <div className="flex justify-between items-center">
            <div className="text-sm">Gold: {selectedCountry.gold}</div>
            <div className="text-sm">Silver: {selectedCountry.silver}</div>
            <div className="text-sm">Bronze: {selectedCountry.bronze}</div>
            <div className="text-sm font-semibold">Total: {selectedCountry.total}</div>
            <div className="text-sm">Athletes: {selectedCountry.athletes_num}</div>
          </div>
        </div>
      )}
    </div>
  );
}

export default DashboardCard02;