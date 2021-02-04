window.cookieconsent.initialise({
  "palette": {
    "popup": {
      "background": "#000",
      "text": "#0f0"
    },
    "button": {
      "background": "#0f0"
    }
  },
  "type": "opt-in",
  "content": {
    "href": "https://thepythoncorner.com/privacy/"
  },
  onInitialise: function (status) {
    var type = this.options.type;
    var didConsent = this.hasConsented();
    if (type == 'opt-in' && didConsent) {
      // enable cookies
      loadGAonConsent();
      loadGADOnConsent();
      loadDisqusOnConsent();  
    }
    if (type == 'opt-out' && !didConsent) {
      // disable cookies
    }
  },
  onStatusChange: function (status, chosenBefore) {
    var type = this.options.type;
    var didConsent = this.hasConsented();
    if (type == 'opt-in' && didConsent) {
      // enable cookies
      loadGAonConsent();
      loadGADOnConsent();
      loadDisqusOnConsent();
    }
    if (type == 'opt-out' && !didConsent) {
      // disable cookies
    }
  },
  onRevokeChoice: function () {
    var type = this.options.type;
    if (type == 'opt-in') {
      // disable cookies
    }
    if (type == 'opt-out') {
      // enable cookies
      loadGAonConsent();
      loadGADOnConsent();
      loadDisqusOnConsent();
    }
  }  
});

