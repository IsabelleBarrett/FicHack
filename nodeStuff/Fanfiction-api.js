var FANFICTION_URL = "https://www.fanfiction.net"

module.exports = {
  getFiction: (id, callback) => {
    var storyUrl = FANFICTION_URL + "/s/" + id

    var request = require("request")
    request(storyUrl, function(error, response, body) {
      var cheerio = require("cheerio")
      var $ = cheerio.load(body)

      var authorHrefRegex = /[0-9]{7}/

      var fictionObject = {
        title: $("#profile_top > b").text(),
        author: $("#profile_top > a").attr("href").match(authorHrefRegex)[0],

      }

      callback(fictionObject)
    })
  }
}
