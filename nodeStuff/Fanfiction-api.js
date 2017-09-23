var FANFICTION_URL = "https://www.fanfiction.net"

module.exports = {
  getFiction: (id, callback) => {
    var storyUrl = FANFICTION_URL + "/s/" + id

    var request = require("request")
    request(storyUrl, function(error, response, body) {
      var cheerio = require("cheerio")
      var $ = cheerio.load(body)

      var fictionObject = {
        title: $("#profile_top > b").text()
      }

      callback(fictionObject)
    })
  }
}
