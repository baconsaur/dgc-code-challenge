from flask import Flask
from flask import jsonify
from flask import request
from flask import json
from itertools import chain
from itertools import combinations

app = Flask(__name__)

def summer(min, max, total):
    return sorted(set(list(chain.from_iterable([
        ['+'.join([str(f) for f in y]) for y in combinations(range(min, max+1), x) if sum(list(y)) == total]
         for x in range(2, len(range(min, max+2)))]))))

@app.route("/findSummer", methods=['PUT'])
def findSummer():
    summer_request = json.loads(request.data)

    result = summer(
        int(summer_request['min']),
        int(summer_request['max']),
        int(summer_request['total']))

    if len(result) > 0:
        return jsonify({'solutions': result})
    return jsonify({'message': 'No solutions'}), 404

if __name__ == "__main__":
    app.run()