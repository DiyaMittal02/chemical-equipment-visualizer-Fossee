import axios from 'axios';

const API_BASE_URL = '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Equipment Dataset APIs
export const uploadCSV = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await axios.post(`${API_BASE_URL}/upload/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    withCredentials: true,
  });

  return response.data;
};

export const getDatasetSummary = async (datasetId) => {
  const response = await api.get(`/summary/${datasetId}/`);
  return response.data;
};

export const getDatasetHistory = async () => {
  const response = await api.get('/history/');
  return response.data;
};

export const getAllDatasets = async () => {
  const response = await api.get('/datasets/');
  return response.data;
};

export const getDataset = async (datasetId) => {
  const response = await api.get(`/datasets/${datasetId}/`);
  return response.data;
};

export const downloadPDF = async (datasetId) => {
  const response = await axios.get(`${API_BASE_URL}/datasets/${datasetId}/download_pdf/`, {
    responseType: 'blob',
    withCredentials: true,
  });
  return response.data;
};

// Authentication APIs
export const registerUser = async (username, password, email) => {
  const response = await api.post('/auth/register/', { username, password, email });
  return response.data;
};

export const loginUser = async (username, password) => {
  const response = await api.post('/auth/login/', { username, password });
  return response.data;
};

export const logoutUser = async () => {
  const response = await api.post('/auth/logout/');
  return response.data;
};

export const getCurrentUser = async () => {
  const response = await api.get('/auth/user/');
  return response.data;
};

export default api;
