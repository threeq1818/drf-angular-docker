export const environment = {
  production: true,
  apiUrl: 'http://localhost/api',
  auth: {
    clientID: 'KCOB2UFoGkiA6qhGSQ8DNi1pbR1YsG56',
    domain: 'dev-rflkcxon.auth0.com',
    audience: 'https://djangularapi',
    auth0RedirectUri: 'http://localhost:4200/callback', // URL to return to after auth0 login
    auth0ReturnTo: 'http://localhost:4200', // URL to return to after auth0 logout
    scope: 'openid profile'
  }
};
