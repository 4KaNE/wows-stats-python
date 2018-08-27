const vm = new Vue({
    el: '#app',
    data: {
      wsdata: {},
      ws: new WebSocket("ws://localhost:8080/websocket")
    },
    mounted: function () {
      this.ws.onmessage = (evt) => {
        this.wsdata = JSON.parse(evt.data)
      }
    }
  })