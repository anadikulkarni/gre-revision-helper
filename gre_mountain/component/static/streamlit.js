// Minimal vanilla-JS implementation of the Streamlit component protocol.
// (Streamlit's own "component without a frontend build" recipe -- no npm needed.)
function _send(type, data) {
  window.parent.postMessage(Object.assign({ isStreamlitMessage: true, type: type }, data), "*");
}

const Streamlit = {
  RENDER_EVENT: "streamlit:render",
  _listeners: {},
  setComponentReady() {
    _send("streamlit:componentReady", { apiVersion: 1 });
  },
  setFrameHeight(height) {
    _send("streamlit:setFrameHeight", { height: height || document.body.scrollHeight });
  },
  setComponentValue(value) {
    _send("streamlit:setComponentValue", { value: value, dataType: "json" });
  },
  events: {
    addEventListener(type, callback) {
      Streamlit._listeners[type] = callback;
      window.addEventListener("message", (event) => {
        if (event.data && event.data.type === type) {
          callback(event);
        }
      });
    },
  },
};
