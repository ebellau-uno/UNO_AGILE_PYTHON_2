"""
Title: api.py
Description: simple api to talk to todo db
Author: Eugene Bellau
Email: ebellau@uno.edu
Date: 3/3/2021
TODO: lint, docs. etc.
"""

import os

#from dotenv import load_dotenv
import dotenv
from flask import Flask, render_template, request, jsonify, abort, Response, redirect
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

app.config["DEBUG"] = True
# this allows for better JSON response from out API
app.config['JSON_SORT_KEYS'] = False

project_folder = os.path.expanduser('~/my_site/UNO_AGILE_PYTHON_2')
dotenv.load_dotenv(os.path.join(project_folder, '.env'))



app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")

mysql = MySQL(app)


@app.route("/v1/all", methods=["GET", "POST"])
def all():
    """
    Title: add.
    Description:
        returns all records in json
    Arguments:
        None
    Returns:
        contects - json - <str>
    Raises:
        None
    """
    if request.method == "POST":
        return "POST not implemented"
    try:
        #data = f'{app.config["MYSQL_USER"]}\n{app.config["MYSQL_PASSWORD"]}\n{app.config["MYSQL_HOST"]}\n{app.config["MYSQL_DB"]}'

        #return data
        # return "All"
        cursor = mysql.connection.cursor()
        query = "SELECT id, name, description, date, importance FROM todo;"
        cursor.execute(query)
        contents = (cursor.fetchall())
        mysql.connection.commit()
        cursor.close()

        data = {}

        for item in contents:
            data[item[0]] = {}
            data[item[0]] ["name"] = item[1]
            data[item[0]] ["description"] = item[2]
            data[item[0]] ["date"] = item[3]
            data[item[0]] ["importance"] = item[4]

        return data
    except Exception as err:
        app.logger.error(err)
        abort(404)



@app.route("/v1/add", methods=["GET", "POST"])
def add():
    """
    Title: add.
    Description:
        returns adds new record
    Arguments:
        request - <str>
            .name - required
            .decription - required
            .date - required
            .importance - required
    Returns:
        MySQL query status - <str>
    Raises:
        None
    """
    if request.method == "POST":
        try:
            data = request.form
            args = ["name", "description", "date", "importance"]
            for arg in args:
                if not data[arg]:
                    return f"{arg} is a required argument"
            name = data["name"]
            description = data["description"]
            date = data["date"]
            importance = data["importance"]
            cursor = mysql.connection.cursor()
            query = "INSERT INTO todo (name, description, date, importance) VALUES (%s, %s, %s, %s);"
            params = [name, description, date, importance]
            cursor.execute(query, params)
            status = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            return redirect("/")
        except Exception as err:
            app.logger.error(err)
            abort(404)
    else:
        try:
            args = ["name", "description", "date", "importance"]
            for arg in args:
                if not request.args.get(arg):
                    return f"{arg} is a required argument"

            app.logger.debug("ARGS are %s", request.args)
            name = request.args.get("name")
            description = request.args.get("description")
            date = request.args.get("date")
            importance = request.args.get("importance")
            cursor = mysql.connection.cursor()
            query = "INSERT INTO todo (name, description, date, importance) VALUES (%s, %s, %s, %s);"
            params = [name, description, date, importance]
            cursor.execute(query, params)
            status = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            return f"{status}"
        except Exception as err:
            app.logger.error(err)
            return err
            abort(404)

@app.route("/v1/update", methods=["GET", "POST"])
def update():
    """
    Title: update.
    Description:
        returns updates record
    Arguments:
        request - <str>
            .name - required
            .decription - required
            .date - required
            .importance - required
    Returns:
        MySQL query status - <str>
    Raises:
        None
    """
    if request.method == "POST":
        try:
            data = request.form
            args = ["name", "description", "date", "importance"]
            for arg in args:
                if not data[arg]:
                    return f"{arg} is a required argument"
            name = data["name"]
            description = data["description"]
            date = data["date"]
            importance = data["importance"]
            cursor = mysql.connection.cursor()
            query = "INSERT INTO todo (name, description, date, importance) VALUES (%s, %s, %s, %s);"
            params = [name, description, date, importance]
            cursor.execute(query, params)
            status = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            return redirect("/")
        except Exception as err:
            app.logger.error(err)
            abort(404)
    else:
        try:
            args = ["name", "description", "date", "importance"]
            for arg in args:
                if not request.args.get(arg):
                    return f"{arg} is a required argument"

            app.logger.debug("ARGS are %s", request.args)
            name = request.args.get("name")
            description = request.args.get("description")
            date = request.args.get("date")
            importance = request.args.get("importance")
            cursor = mysql.connection.cursor()
            query = "INSERT INTO todo (name, description, date, importance) VALUES (%s, %s, %s, %s);"
            params = [name, description, date, importance]
            cursor.execute(query, params)
            status = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            return f"{status}"
        except Exception as err:
            app.logger.error(err)
            abort(404)

@app.route("/v1/delete", methods=["GET", "POST"])
def delete():
    """
    Title: delete.
    Description:
        returns updates record
    Arguments:
        request - <str>
            .id - required
    Returns:
        MySQL query status - <str>
    Raises:
        None
    """
    if request.method == "POST":
        try:
            data = request.form
            args = ["id"]
            for arg in args:
                if not data[arg]:
                    return f"{arg} is a required argument"
            id = data["id"]
            cursor = mysql.connection.cursor()
            query = "DELETE FROM todo WHERE id=%s;"
            params = [id]
            cursor.execute(query, params)
            status = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            return redirect("/")
        except Exception as err:
            app.logger.error(err)
            abort(404)
    else:


        try:
            args = ["id"]
            for arg in args:
                if not request.args.get(arg):
                    return f"{arg} is a required argument"

            app.logger.debug("ARGS are %s", request.args)
            id= request.args.get("id")
            cursor = mysql.connection.cursor()
            query = "DELETE FROM todo WHERE id=%s;;"
            params = [id]
            cursor.execute(query, params)
            status = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            return f"{status}"
        except Exception as err:
            app.logger.error(err)
            abort(404)

if __name__ == "__main__":
    app.run()
