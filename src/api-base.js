class ApiBase {
   constructor(props) {
      const p = props || {};
      this.baseUrl = p['baseUrl'] || "http://localhost:8060/";
      this.endPoints = p['endPoints'] || {};
   }

   callify() {
      for (let p in this.endPoints) {
         if (this.endPoints.hasOwnProperty(p)) {
            const ep = this.endPoints[p];
         }
      }
   }

   fetch(url, method) {

   }
}

export default ApiBase;