import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.esm.browser.js';

const apiRoot = `${window.origin}/api/v1/product`

const app = new Vue({
  el: '#app',
  data: {
    message: '',
    q: '',
    offset: 0,
    limit: 10,
    products: [],
    totalProducts: 0,
  },
  methods: {
    indexProducts: async function() {
      console.log('Indexing...');
      this.message = 'Indexing...';
      try {
        const response = await fetch(`${apiRoot}/index`);
        const json = await response.json();
        console.log(json['message']);
        this.message = json['message'];

      } catch (e) {
        console.log(e);
        this.message = e.message;
      }
    },
    searchProducts: async function() {
      this.message = 'Searching...';
      console.log(`Requesting products with search parameters: q = ${this.q}, offset = ${this.offset}, limit = ${this.limit}`);
      try {
        const response = await fetch(`${apiRoot}/search?q=${this.q}&offset=${this.offset}&limit=${this.limit}`);
        const json = await response.json();
        this.products = json['products'];
        this.totalProducts = json['totalProducts'];
        this.message = '';

      } catch (e) {
        console.log(e);
        this.message = e.message;
      }
    },
    getPreviousProducts: function() {
      this.computedOffset -= 10;
      this.searchProducts();
    },
    getNextProducts: function() {
      this.computedOffset += 10;
      this.searchProducts();
    },
  },
  computed: {
    computedOffset: {
      get: function() {
        return this.offset;
      },
      set: function(value) {
        if (value < 0) {
          value = 0;
        }
        this.offset = value;
      }
    }
  },
  created: async function() {
    this.indexProducts();
  }
});
