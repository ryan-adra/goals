#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
from goalsDatabase import CreateGoal

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.write(template.render())

# class CreateUser(webbapp2.RequestHandler):
#     def get(self):
#
#
class CreateGoals(webapp2.RequestHandler):
     def get(self):
        #goal1 = CreateGoal(goal ="The first goal")
        template = env.get_template('main.html')
        self.response.write(template.render())

     def post(self):
        results_templates = env.get_template('results.html')

        goal = CreateGoal(goal=self.request.get('goal'),
                          timeHours= int(self.request.get('hour')),
                          timeMinutes =  int(self.request.get('minutes'))
                         ).put()
        goal_display = goal.get()
        self.response.write(results.html.render(goal_display))
        #goal = CreateGoal(goal=self.request.get('goal')).put()
        # VideoRating(id = 'Gangnam Style',likes = 133,dislikes = 23).put()
        # VideoRating(id = 'Cuet Cats',likes = 1234,dislikes = 24).put()
        # VideoRating(id = 'Cute dogs',likes = 345,dislikes = 21).put()
        # VideoRating(id = 'Weird AI',likes = 21445,dislikes = 0).put()
        #
        self.response.write('Done')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create_goal',CreateGoals)
], debug=True)
