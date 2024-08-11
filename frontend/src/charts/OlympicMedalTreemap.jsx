import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import axios from '../api';

const OlympicMedalTreemap = () => {
  const svgRef = useRef(null);
  const tooltipRef = useRef(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('top_countries_athletes/');
        const data = response.data;
        createVisualization(data.top_countries);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const createVisualization = (countries) => {
    const width = 800;
    const height = 600;

    const svg = d3.select(svgRef.current)
      .attr('width', width)
      .attr('height', height);

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
        showAthletes(d.data);
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

  const showAthletes = (country) => {
    const athletesContainer = d3.select('#athletes-container');
    athletesContainer.html('');

    athletesContainer.append('h3')
      .text(`${country.country_code} - Top Athletes`);

    const athleteList = athletesContainer.append('ul');

    country.athletes.forEach(athlete => {
      const athleteItem = athleteList.append('li');
      athleteItem.append('strong').text(athlete.name);
      const medalList = athleteItem.append('ul');

      athlete.medals.forEach(medal => {
        medalList.append('li')
          .html(`${getMedalEmoji(medal.medal_type)} ${medal.event} (${medal.discipline})`);
      });
    });
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
        <div id="athletes-container" className="mt-4 xl:mt-0 xl:ml-4 flex-grow overflow-auto max-h-96"></div>
      </div>
      <div ref={tooltipRef} className="absolute bg-white dark:bg-gray-700 p-2 rounded shadow-md opacity-0 pointer-events-none"></div>
    </div>
  );
};

export default OlympicMedalTreemap;