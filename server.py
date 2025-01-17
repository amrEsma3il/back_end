from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/.well-known/assetlinks.json', methods=['GET'])
def assetlinks():
    assetlinks_data = [
        {
            "relation": ["delegate_permission/common.handle_all_urls"],
            "target": {
                "namespace": "android_app",
                "package_name": "com.example.deep_link",
                "sha256_cert_fingerprints": [
                    "95:98:95:92:1F:92:28:BE:FD:C5:AC:5A:49:75:64:42:B8:B3:99:7B:91:97:D6:BE:06:B1:2E:5A:E7:E9:BC:9D"
                ]
            }
        }
    ]
    return jsonify(assetlinks_data)

if __name__ == '__main__':
    app.run(debug=True)
