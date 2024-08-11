import Axios from "axios";

let BACKEND_SERVER = null;
if (window.location.origin === "http://localhost:5173") {
  BACKEND_SERVER = "http://127.0.0.1:8000/api/v1/";
} else {
  BACKEND_SERVER = window.location.origin + "/api/v1/";
}

export const API_SERVER = BACKEND_SERVER;

const axios = Axios.create({
  baseURL: `${API_SERVER}`,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

// Add a request interceptor
axios.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor remains the same
axios.interceptors.response.use(
  (response) => Promise.resolve(response),
  (error) => {
    // You could add logic here to refresh the token if it's expired
    return Promise.reject(error);
  }
);

export default axios;