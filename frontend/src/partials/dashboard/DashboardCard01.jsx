import React, { useState, useEffect } from 'react';
import axios from '../../api/index';

function DashboardCard01() {
    const [data, setData] = useState({
        participants_count: 0,
        countries_count: 0,
        medals_count: 0,
        events_count: 0
    });

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('general_stats/');
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="flex flex-col col-span-full sm:col-span-6 xl:col-span-3 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
            <div className="px-5 pt-5 pb-5">
                <header className="flex justify-between items-start mb-2">
                    <h2 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">Olympic Statistics</h2>
                </header>
                <div className="grid grid-cols-2 gap-4">
                    <div>
                        <div className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase mb-1">Participants</div>
                        <div className="text-2xl font-bold text-gray-800 dark:text-gray-100">{data.participants_count.toLocaleString()}</div>
                    </div>
                    <div>
                        <div className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase mb-1">Countries</div>
                        <div className="text-2xl font-bold text-gray-800 dark:text-gray-100">{data.countries_count}</div>
                    </div>
                    <div>
                        <div className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase mb-1">Medals</div>
                        <div className="text-2xl font-bold text-gray-800 dark:text-gray-100">{data.medals_count.toLocaleString()}</div>
                    </div>
                    <div>
                        <div className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase mb-1">Events</div>
                        <div className="text-2xl font-bold text-gray-800 dark:text-gray-100">{data.events_count}</div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default DashboardCard01;