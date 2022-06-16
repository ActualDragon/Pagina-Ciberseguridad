import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url'; // Needed to work with path.
import { v4 as uuid } from 'uuid';
import methodOverride from 'method-override';
import fs from 'fs';
// This following import is experimental, it might not work in the future.
import tweetDataJSON from './data.json' assert { type: 'json'}; // Needed when using ESM, import expects JS code by default.

// We add __filename to get the current path.
const __filename = fileURLToPath(import.meta.url);
// We add __dirname to our ES scope.
const __dirname = path.dirname(__filename);
// Express server variable.
const app = express();
// We pass JSON data to a variable we can edit.
let tweetData = tweetDataJSON.tweets;

// We serve our static files to any the request.
app.use(express.static(path.join(__dirname, 'public')));
// Middleware to parse request as URL encoded.
app.use(express.urlencoded({ extended: true }));
// Middleware to parse JSON requests.
app.use(express.json());
// We tell our app to use EJS.
app.set('view engine', 'ejs');
// We set the path of our views folder.
app.set('views', path.join(__dirname, 'views'));
// We call in the override functionallity.
app.use(methodOverride('_method'));

/* What follows are all of our API movements. */
app.get('/', (req, res) => {
    res.render('home', { title: 'Home' })
});

/* Load page containing all tweets. */
app.get('/tweets', (req, res) => {
    res.render('tweets/index', { title: 'All tweets', tweets: tweetData })
});

/* Load page containing form to add new tweet. */
app.get('/tweets/new', (req, res) => {
    res.render('tweets/new', { title: 'New tweet' }); // File to render on request.
});

/* Request to add new tweet. */
app.post('/tweets/new', (req, res) => {
    const { username, tweet } = req.body;
    const data = { username, tweet, id: uuid() };
    tweetData.push(data);
    console.log(`Tweet from ${username} registered!`);
    res.redirect('/tweets'); // This calls the GET for '/tweets' file.
});

/* Load page with single tweet. */
app.get('/tweets/:id', (req, res) => {
    const { id } = req.params;
    const tweet = tweetData.find(t => t.id == id);
    res.render('tweets/show', { title: 'Tweet!', tweet })
});

/* Loas page for edit. */
app.get('/tweets/:id/edit', (req, res) => {
    const { id } = req.params;
    const tweet = tweetData.find(t => t.id == id);
    res.render('tweets/edit', { title: "Edit tweet", tweet });
});

/* Request to edit tweet content. */
app.patch('/tweets/:id', (req, res) => {
    const { id } = req.params;
    const newTweet = req.body.tweet; // If using PUT we can't do this partially.
    const foundTweet = tweetData.find(t => t.id == id);
    foundTweet.tweet = newTweet;
    res.redirect('/tweets');
});

/* Request to delete tweet. */
app.delete('/tweets/:id', (req, res) => {
    let { id } = req.params;
    // Check if variable id is a string and if so change it to a number.
    if (id === "1" || id === "2" || id === "3") id = parseInt(id);
    // We delete with a filter to avoid mutations.
    tweetData = tweetData.filter(t => t.id !== id);
    console.log(`Tweet with id = "${id}" deleted!`);
    res.redirect('/tweets');
});

// We assign a port to our server.
app.listen(8080, () => {
    console.log("Listening on port 8080.")
});
