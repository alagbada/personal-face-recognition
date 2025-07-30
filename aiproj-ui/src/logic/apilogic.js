import axios from "axios";

export async function predictImage(base64Str) {
    const url = 'http://127.0.0.1:5000/predict-base64-image';
    const formData = new FormData();
    formData.append('base64_img', base64Str);
    const response = await axios.post(url, formData);
    return response.data
}