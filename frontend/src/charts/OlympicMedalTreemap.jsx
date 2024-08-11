import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import axios from '../api';

const OlympicMedalTreemap = () => {
  const svgRef = useRef(null);
  const tooltipRef = useRef(null);
  const [countries, setCountries] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState(null);
  const [sports, setSports] = useState([]);
  const [selectedSport, setSelectedSport] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('top_countries_athletes/');
        const data = response.data;
        setCountries(data.top_countries);
        createVisualization(data.top_countries);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    if (selectedCountry) {
      const uniqueSports = new Set();
      selectedCountry.athletes.forEach(athlete => {
        athlete.medals.forEach(medal => {
          uniqueSports.add(medal.discipline);
        });
      });
      setSports(Array.from(uniqueSports).sort());
      setSelectedSport('');
    }
  }, [selectedCountry]);

  const createVisualization = (countries) => {
    const width = 800;
    const height = 600;

    const svg = d3.select(svgRef.current)
      .attr('width', width)
      .attr('height', height);

    svg.selectAll("*").remove(); // Clear previous rendering

    const tooltip = d3.select(tooltipRef.current);

    const treemapLayout = d3.treemap()
      .size([width, height])
      .paddingOuter(1)
      .paddingInner(1);

    const root = d3.hierarchy({ children: countries })
      .sum(d => d.total);

    treemapLayout(root);

    const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

    // Country rectangles
    svg.selectAll('rect')
      .data(root.leaves())
      .enter()
      .append('rect')
      .attr('x', d => d.x0)
      .attr('y', d => d.y0)
      .attr('width', d => d.x1 - d.x0)
      .attr('height', d => d.y1 - d.y0)
      .attr('fill', d => colorScale(d.data.country_code))
      .attr('stroke', 'white')
      .on('mouseover', (event, d) => {
        tooltip.style('opacity', 1)
          .html(`<strong>${d.data.country_code}</strong><br/>Total Medals: ${d.data.total}`)
          .style('left', (event.pageX + 10) + 'px')
          .style('top', (event.pageY - 10) + 'px');
      })
      .on('mouseout', () => {
        tooltip.style('opacity', 0);
      })
      .on('click', (event, d) => {
        setSelectedCountry(d.data);
      });

    // Country labels
    svg.selectAll('text')
      .data(root.leaves())
      .enter()
      .append('text')
      .attr('x', d => d.x0 + 5)
      .attr('y', d => d.y0 + 20)
      .text(d => d.data.country_code)
      .attr('font-size', '16px')
      .attr('fill', 'white');
  };

  const renderAthletes = () => {
    if (!selectedCountry || !selectedSport) return null;

    const athletesInSport = selectedCountry.athletes.filter(athlete =>
      athlete.medals.some(medal => medal.discipline === selectedSport)
    );

    const sortedAthletes = athletesInSport.sort((a, b) => {
      const medalOrder = { 'Gold Medal': 3, 'Silver Medal': 2, 'Bronze Medal': 1 };
      const aMedalValue = Math.max(...a.medals.filter(m => m.discipline === selectedSport).map(m => medalOrder[m.medal_type]));
      const bMedalValue = Math.max(...b.medals.filter(m => m.discipline === selectedSport).map(m => medalOrder[m.medal_type]));
      return bMedalValue - aMedalValue;
    });

    return (
      <ul className="mt-4">
        {sortedAthletes.map((athlete, index) => (
          <li key={index} className="mb-2">
            <strong>{athlete.name}</strong>
            <ul className="ml-4">
              {athlete.medals
                .filter(medal => medal.discipline === selectedSport)
                .sort((a, b) => {
                  const order = { 'Gold Medal': 3, 'Silver Medal': 2, 'Bronze Medal': 1 };
                  return order[b.medal_type] - order[a.medal_type];
                })
                .map((medal, mIndex) => (
                  <li key={mIndex}>
                    {getMedalEmoji(medal.medal_type)} {medal.event}
                  </li>
                ))}
            </ul>
          </li>
        ))}
      </ul>
    );
  };

  const getMedalEmoji = (medalType) => {
    switch (medalType) {
      case 'Gold Medal': return '🥇';
      case 'Silver Medal': return '🥈';
      case 'Bronze Medal': return '🥉';
      default: return '';
    }
  };

  return (
    <div className="flex flex-col col-span-full xl:col-span-12 bg-white dark:bg-gray-800 shadow-sm rounded-xl p-4">
      <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-4">Top 5 Countries Olympic Performance</h2>
      <div className="flex flex-col xl:flex-row">
        <svg ref={svgRef}></svg>
        <div className="mt-4 xl:mt-0 xl:ml-4 flex-grow">
          {selectedCountry && (
            <>
              <h3 className="text-md font-semibold mb-2">{selectedCountry.country_code} - Select a Sport</h3>
              <select
                value={selectedSport}
                onChange={(e) => setSelectedSport(e.target.value)}
                className="w-full p-2 border rounded mb-4 dark:bg-gray-700 dark:text-white"
              >
                <option value="">Select a sport</option>
                {sports.map((sport, index) => (
                  <option key={index} value={sport}>{sport}</option>
                ))}
              </select>
              {renderAthletes()}
            </>
          )}
        </div>
      </div>
      <div ref={tooltipRef} className="absolute bg-white dark:bg-gray-700 p-2 rounded shadow-md opacity-0 pointer-events-none"></div>
    </div>
  );
};

export default OlympicMedalTreemap;