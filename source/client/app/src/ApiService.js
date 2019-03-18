import axios from 'axios'

const API_URL = 'http://192.168.99.101'

export class APIService {
    constructor() {

    }

    getPlataformas() {
        const url = `${API_URL}/api/plataformas`;
        return axios.get(url).then(response => response.data);
    }

    updatePlataformas(plataforma) {
        const url = `${API_URL}/api/plataformas/${plataforma.id}/`;
        console.log('PUT', plataforma)
        return axios.put(url,plataforma);
    }

    deletePlataformas(pk){
        const url = `${API_URL}/api/plataformas/${pk}`;
        return axios.delete(url);
    }

    createPlataformas(plataforma){

        const url = `${API_URL}/api/plataformas/`;
        return axios.post(url,plataforma);
    }
}