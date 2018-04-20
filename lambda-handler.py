#!/usr/bin/env python2
import re

definitions = {
    # Concept : [Definition, Example] ("": ["", ""],)
    # Unit 1
    "calculus": ["Calculus is the mathematical study of continuous change, in the same way that geometry is the study of shape and algebra is the study of generalizations of arithmetic operations", " if you had one formula telling how much money you got every day, calculus would help you understand related formulas like how much money you have in total, and whether you are getting more money or less than you used to"],
    "function": ["A function is an equation will be a function if for any x in the domain of the equation, the equation will yield exactly one value of y.", "Y equals X squared plus one"],
    "functions": ["Functions are equations will be a function if for any x in the domain of the equation, the equation will yield exactly one value of y.", "Y equals X squared plus one"],
    "limit": ["A limit is the value that a function or sequence approaches as the input or index approaches some value. Limits can be analysed through the use of tables, graphs, or algebraicly.", "the limit of f of n as n approaches c equals L"],
    "limits": ["Limits are the values that a function or sequence approaches as the input or index approaches some value. Limits can be analysed through the use of tables, graphs, or algebraicly.", "the limit of f of n as n approaches c equals L"],
    "continuity": ["A function is said to be continuous if it is continuous at every point of the interval x and y.", "A function f of x is said to be continuous at x equals a if the limit of f of x as x approaches a equals f of a"],
    "continuous function": ["A continuous function is a function for which sufficiently small changes in the input result in arbitrarily small changes in the output.", ""],
    "discontinuity": ["When a function is not continuous at a point, then we can say it is discontinuous at that point.", "The function f of x equals 1 over x minus 1 is not continuous when x equals 1"],
    "discontinuous function": ["A Discontinuous function is a function that is not a continuous curve, meaning that it has points that are isolated from each other on a graph.", "The function f of x equals 1 over x minus 1 is not continuous when x equals 1"],
    "removable discontinuity": ["A removable discontinuity is a point at which a graph is not connected but can be made connected by filling in a single point.", "when the limit of f of x as x approaches a exists and either f of a is undefined or the limit of f of x as x approaches a is not equal to f of a"],
    "essential discontinuity": ["A essential discontinuity is any discontinuity that is not removable", ""],
    "infinite discontinuity": ["A function creates an Infinite Discontinuity at a if any of the one or two sided limits at a is infinite.", ""],
    "hole": ["A hole is another name for a removable discontinuity or removable singularity.", ""],
    # Unit 2
    "asymptote": ["An asymptote is a line that a graph approaches, but does not intersect.", "y equals 4 x plus 2 over x squared plus 1"],
    "asymptotes": ["An asymptote is a line that a graph approaches, but does not intersect.", "y equals 4 x plus 2 over x squared plus 1"],
    "vertical asymptote": ["Vertical asymptotes are vertical lines which correspond to the zeroes of the denominator of a rational function.", "X cannot be negative 3 or negative 2."],
    "vertical asymptotes": ["Vertical asymptotes are vertical lines which correspond to the zeroes of the denominator of a rational function.", "X cannot be negative 3 or negative 2."],
    "horizontal asymptote": ["Horizontal asymptotes are horizontal lines that the graph of the function approaches as x approaches positive or a negative infinity.", "y equals c if the limit as x approaches inifity of f of x equals c or if the limit as x approaches possitive inifity of f of x equals c "],
    "horizontal asymptotes": ["Horizontal asymptotes are horizontal lines that the graph of the function approaches as x approaches positive or a negative infinity.", "y equals c if the limit as x approaches inifity of f of x equals c or if the limit as x approaches possitive inifity of f of x equals c "],
    "oblique asymptote": ["an oblique asymptote occurs when a linear asymptote is not parallel to the x and y axis.", "y equals negative two x minus 4"],
    "oblique asymptotes": ["oblique asymptotes occurs when linear asymptotes are not parallel to the x and y axis.", "y equals negative two x minus 4"],
    "slant asymptote": ["an oblique or slant asymptote occurs when a linear asymptote is not parallel to the x and y axis.", "y equals negative two x minus 4"],
    "slant asymptotes": ["oblique asymptotes or slant asymptotes occurs when linear asymptotes are not parallel to the x and y axis.", "y equals negative two x minus 4"],
    "derivative": ["The derivative of a function of a real variable measures the sensitivity to change of the function value with respect to a change in its argument.", "when f of x equals x cubed, f prime equals three x squared"],
    "derivatives": ["Derivatives of a function of a real variable measures the sensitivity to change of the function value with respect to a change in its argument.", "when f of x equals x cubed, f prime equals three x squared"],
    "properties of derivatives": ["The properties of derivatives are rules that applie to all derivatives", "the power rule"],
    "power rule": ["The power rule is used to differentiate functions of the form f equals x to the power of r, whenever r is a real number", "when f of x equals x cubed, f prime equals three x squared"],
    "power rule for derivatives": ["The power rule is used to differentiate functions of the form f equals x to the power of r, whenever r is a real number", "when f of x equals x cubed, f prime equals three x squared"],
    "sum/difference rule": ["the sum rule in differentiation is a method of finding the derivative of a function that is the sum of two other functions for which derivatives exist.", "the derivative of f plus g is f prime plus g prime"],
    "sum/difference rule for derivatives": ["the sum rule in differentiation is a method of finding the derivative of a function that is the sum of two other functions for which derivatives exist.", "the derivative of f plus g is f prime plus g prime"],
    "sum rule": ["the sum rule in differentiation is a method of finding the derivative of a function that is the sum of two other functions for which derivatives exist.", "the derivative of f plus g is f prime plus g prime"],
    "sum rule for derivatives": ["the sum rule in differentiation is a method of finding the derivative of a function that is the sum of two other functions for which derivatives exist.", "the derivative of f plus g is f prime plus g prime"],
    "difference rule": ["the sum rule in differentiation is a method of finding the derivative of a function that is the sum of two other functions for which derivatives exist.", "the derivative of f minus g is f prime minus g prime"],
    "difference rule for derivatives": ["the sum rule in differentiation is a method of finding the derivative of a function that is the sum of two other functions for which derivatives exist.", "the derivative of f minus g is f prime minus g prime"],
    "product rule": ["The product rule is used to find the derivative of a product of two functions.", "the derivative of f time g is f times g prime plus f prime times g"],
    "product rule for derivatives": ["The product rule is used to find the derivative of a product of two functions.", "the derivative of f time g is f times g prime plus f prime times g"],
    "quotient rule": ["The quotient rule gives the derivative of one function divided by another.", "the derivative of f over g is f times g prime minus f prime times g all over g squared"],
    "quotient rule for derivatives": ["The quotient rule gives the derivative of one function divided by another.", "the derivative of f over g is f times g prime minus f prime times g all over g squared"],
    "derivatives of exponential functions": ["", "the derivative of e to the power of x is e to the power of x"],
    "derivatives of logarithmic functions": ["", ""],
    "derivatives of trigonometric functions": ["", ""],
    # Unit 3
    "implicit differentiation": ["Implicit differentiation is nothing more than a special case of the well-known chain rule for derivatives", "x squared plus y squared equals twenty five"],
    "inverse derivative": ["the inverse of a function y equals f of x is a function that, in some fashion, undoes the effect of f", "x equals f inverse of y is the inverse of y equals f or x"],
    "inverse derivatives": ["the inverse of a function y equals f of x is a function that, in some fashion, undoes the effect of f", "x equals f inverse of y is the inverse of y equals f or x"],
    "critical point": ["the critical point is where if the value goes above or below it will lead to significant change in other values", "f prime of x equals 3 x squared minus 3 its two critical points at x equals negative 1 and positive 1"],
    "critical points": ["critical points is where if the value goes above or below it will lead to significant change in other values", "f prime of x equals 3 x squared minus 3 its two critical points at x equals negative 1 and positive 1"],
    "local extrema": ["the local extrema is the maximum or minimum in the area that occurs around a point", "the maximum is x equals 14"],
    "local extremas": ["the local extremas are the maximum or minimums in the area that occurs around a point", "the maximum is x equals 14 and the minimum is x equals 5"],
    "absolute extrema": ["absolute extrema are nothing more than the largest and smallest values that a function will take so all that we really need to do is get a list of possible absolute extrema", "the maximum is x equals 14"],
    "absolute extremas": ["absolute extremas are nothing more than the largest and smallest values that a function will take so all that we really need to do is get a list of possible absolute extrema", "the maximum is x equals 14 and the minimum is x equals 5"],
    "inflection points": ["an inflection point, point of inflection, flex, or inflection is a point on a curve at which the curve changes from being concave to convex, or vice versa", "when f of x equals x cubed the inflection point is at 0"],
    "concavity": ["concavity is the shape of the curvature of a function", "if f of x is 2 the it is concave up"],
    "L'Hopital's rule": ["L'Hospital's rule uses derivatives to help evaluate limits involving indeterminate forms", "the derivative of 3 x squared plus x all over 5 x sqaured plus 12 x is 6 x plus 1 all over 10 x plus 12. This still doesn't work. You have to take the derivative again. It is 6 over 10. This works "],
    # Unit 4
    "tangent line": ["the tangent line to a plane curve at a given point is the straight line that just touches the curve at that point.", ""],
    "tangent lines": ["tangent lines to a plane curve at a given point is the straight line that just touches the curve at that point.", ""],
    "normal line": ["The normal line to a curve at a particular point is the line through that point and perpendicular to the tangent", ""],
    "normal lines": ["The normal line to a curve at a particular point is the line through that point and perpendicular to the tangent", ""],
    "approximation": ["an approximation is a inexact result adequate for a given purpose.", ""],
    "approximations": ["approximations are inexact results adequate for a given purpose.", ""],
    "differential": ["the differential represents the principal part of the change in a function y equals f of x with respect to changes in the independent variable.", ""],
    "differentials": ["differentials represents the principal part of the change in a function y equals f of x with respect to changes in the independent variable.", ""],
    "related rate": ["the related rate involves finding a rate at which a quantity changes by relating that quantity to other quantities whose rates of change are known.", ""],
    "related rates": ["related rates problems involve finding a rate at which a quantity changes by relating that quantity to other quantities whose rates of change are known.", ""],
    "optimization": ["optimization is the the mathematical procedures such as finding the maximum of a function", ""],
    # Unit 5
    "Reimann sum": ["the Reimannsum is a certain kind of approximation of an integral by a finite sum.", "if we wanted to compute the area under the curve f of x equals negative x squared plus 3 on the interval 1 comma 3."],
    "right endpoint rule": ["the right endpoint rule is using the right endpoint or side of the rectangle to find an approximation of the area under a curve", "the sum of f of x sub i minus 1 as i approaches n delta x"],
    "left endpoint rule": ["the left endpoint rule is using the left endpoint or side of the rectangle to find an approximation of the area under a curve", "the sum of f of x sub i as i approaches n delta x"],
    "midpoint rule": ["the midpoint rule is using the midpoint of the rectangle to find an approximation of the area under a curve", "delta x of the right endpoint and the left endpoint"],
    "definite integral": ["A Definite Integral has start and end values: in other words there is an interval (a to b)", "intergral of f of x is dx"],
    "integral": ["an integral assigns numbers to functions in a way that can describe displacement, area, volume, and other concepts that arise by combining infinitesimal data", "the area under f of x from 0 to ax"],
    "antiderivative": ["an antiderivative, primitive function, primitive integral or indefinite integral of a function is a differentiable function whose derivative is equal to the original function.", "f of x equals x cubed divided by 3 has the derivative of f of x equals x squared meaning the antiderivative is f"],
    "indefinite integral": ["The function f of x, the function being integrated, is known as the integrand. Note that the indefinite integral yields a family of functions one being an indefinite intergral", "intergral of f of x is dx plus C"],
    # Unit 6
    "u-substitution for integration": ["u-substitution is used when an integral contains some function and its derivative, that is, for an integral of the form.", "The integration is achieved by rewriting the integral in a form that makes it easier to read. Here, let u equals f of x. Then du over dx equals f prime of x"],
    "integration by parts": ["integration by parts or partial integration is a process that finds the integral of a product of functions in terms of the integral of their derivative and antiderivative.", "f u equals u of x and du equals u prime of x dx, while v equals v of x and dv equals v prime of x dx, then integration by parts states that: the integreal of u times dv equals uv minus the integral of v times du"],
    "partial fraction decomposition": ["partial fraction decomposition is the operation that consists in expressing the fraction as a sum of a polynomial and one or several fractions with a simpler denominator.", ""],
    "integration by partial fraction decomposition": ["Partial fraction decomposition can help you with differential equations of the following form: dx over dt equals (x minus a) times (x minus b)", ""],
    # Unit 7
    "determine the area between curves": ["a method of determining the area between two curves", "Given are the two curves y equals f of x and y equals g of x. equating both the curves to get the value of interval [a,b] where the given curves intersects. The area between the two curves bounded by the x axis is given by the formula A equals the intergral of a and b of f of x minus g of x dx"],
    "solid of revolution": ["a solid of revolution is a solid figure obtained by rotating a plane curve around some straight line that lies on the same plane.", ""],
    "volume of a solid of revolution": ["the volume of a solid of revolution", "V equals intergral from a to b equals A of x dx"],
    "disk method": ["a method of finding the volume of a solid that revolves directly around the axis of rotation", ""],
    "washer method": ["a method of finding the volume of a solid that revolves around the axis of rotation without touching the axis", ""],
    "cylindrical shell method": ["a method of cylindrical shells, that is easier to use in such a case.", "Using cylindrical shell with inner radius, outer radius, and height. Its volume is calculated by subtracting the volume of the inner cylinder from the volume of the outer cylinder"],
    # Unit 8
    "differential equations": ["A differential equation is a mathematical equation that relates some function with its derivatives.", "the functions usually represent physical quantities, the derivatives represent their rates of change, and the equation defines a relationship between the two. "],
    "arc length": ["The distance along the curved line making up the arc", ""]
}


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    cleanr = re.compile('<.*?>')
    cardContent = re.sub(cleanr, '', output).title()
    print("OUTPUT: " + cardContent)
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': cardContent
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "<speak>Welcome to the Calculus Helper Alexa Skill, Ask me a question like: What are limits?</speak>"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = "<speak>Ask me a question like: What are limits?</speak>"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "<speak>Good bye</speak>"
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def notFound(concept):
    card_title = "Error"
    if not concept or concept == "" or concept == "":
        speech_output = "<speak>I could not find that one. Can I help you with anything else?</speak>"
    else:
        speech_output = "<speak>I could not find <emphasis level=\"moderate\">%s</emphasis>. Can I help you with anything else?</speak>" % concept
    should_end_session = False
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def conceptIntent(intent_request):
    try:
        concept = intent_request['intent']['slots']['concept']['value']
    except Exception as e:
        print(str(e))
        return notFound(None)
    try:
        card_title = "Info"
        speech_output = "<speak>%s An example would be <emphasis level=\"moderate\">%s</emphasis>. Can I help you with anything else?</speak>" % (
            definitions[concept][0], definitions[concept][1])
        should_end_session = False
        return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))
    except Exception as e:
        print(str(e))
        return notFound(concept)
    return notFound(None)


def definitionIntent(intent_request):
    try:
        concept = intent_request['intent']['slots']['concept']['value']
    except Exception as e:
        print(str(e))
        return notFound(None)
    try:
        card_title = "Info"
        speech_output = "<speak>%s. Can I help you with anything else?</speak>" % (
            definitions[concept][0])
        should_end_session = False
        return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))
    except Exception as e:
        print(str(e))
        return notFound(concept)
    return notFound(None)


def exampleIntent(intent_request):
    try:
        concept = intent_request['intent']['slots']['concept']['value']
    except Exception as e:
        print(str(e))
        return notFound(None)
    try:
        card_title = "Info"
        speech_output = "<speak>An example of %s would be <emphasis level=\"moderate\">%s</emphasis>. Can I help you with anything else?</speak>" % (
            concept, definitions[concept][1])
        should_end_session = False
        return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))
    except Exception as e:
        print(str(e))
        return notFound(concept)
    return notFound(None)


def yesIntent():
    card_title = "How can I help you?"
    speech_output = "<speak>How can I help you?</speak>"
    should_end_session = False
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def on_session_started(session_started_request, session):
    print("START on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    print("LAUNCH on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()


def on_intent(intent_request, session):
    intent_name = intent_request['intent']['name']

    print("INTENT " + intent_name + " requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    if intent_name == "conceptIntent":
        return conceptIntent(intent_request)
    if intent_name == "definitionIntent":
        return definitionIntent(intent_request)
    if intent_name == "exampleIntent":
        return exampleIntent(intent_request)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.YesIntent":
        return yesIntent()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent" or intent_name == "AMAZON.NoIntent":
        return handle_session_end_request()
    else:
        #raise ValueError("Invalid intent")
        return get_help_response()


def on_session_ended(session_ended_request, session):
    print("END on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if (event['session']['application']['applicationId'] != "amzn1.ask.skill.472f92d7-1b88-42ca-be0b-a6f7d077c38e"):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
