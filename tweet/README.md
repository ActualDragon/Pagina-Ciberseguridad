# Tweet generator

> Code of a very basic NodeJS project that I did along side a web development course. This code uses the Express framework to create a server.

**Generic:** This code has be run using NodeJS, it is not meant to be a website. It was made for didactical reasons and uses a bunch of different NodeJS packages to work. The purpose of this code is to consolidate all the things I´ve been shown in the course so far.

**Specific:** This code works and should be run in the browser and it is set to 'localhost:8080/'. It is a Twitter mockup that only allows you to create tweets and manipulate them with CRUD functionality using RESTful routes and APIs. It does not do any user authentication, it's only focused on manipulating tweets.

## Technical details

To run this code first run the following command while on this directory level:

``` sh
npm install
```

This will download all required packages based on the package.json file contained in this repository. To run npm commands you have to download [NodeJS](https://nodejs.org/en/).

Used packages:
- EJS
- Express
- Method-Override
- UUID

Once you've got the project in your computer run the program as follows and open 'localhost:8080' in your browser.

``` sh
nodemon index.js
```

For this command to work the Nodemon package must be installed, it's recommended to install this as a global package. The installation command goes as follows:

``` sh
npm install -g nodemon
```

Bootstrap was used to format this website, the CDN was ignored and more focus was given to downloading the files locally. This files can be found in the 'public' directory and the version we used was [Bootstrap v5.2.0-beta1](https://getbootstrap.com/docs/5.2/getting-started/download/). Besides this some small proprietary CSS classes were built and they can be found in the 'styles.css' file contained in this same directory.