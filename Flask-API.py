import random
from flask import *

app = Flask(__name__)

@app.route('/make-page/', methods=['GET'])
def makenewpage():

    name = str(request.args.get('name'))
    discription = str(request.args.get('discription'))
    locashion = str(request.args.get('locashion'))

    instagram = str(request.args.get('instagram'))
    snapchat = str(request.args.get('snapchat'))
    telegram = str(request.args.get('telegram'))
    twitter = str(request.args.get('twitter'))

    nums = '1234567890'
    abcd = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    the_ran_name = random.choice(abcd) + random.choice(abcd) + random.choice(abcd) + random.choice(abcd) + random.choice(nums) + random.choice(nums) +  random.choice(nums) + random.choice(abcd) + '.html'

    data = f'''
<!DOCTYPE html>
<html>
    <head>
        <title>{name}</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/main.css">
        <link rel="shortcut icon" type="image/png" href="image/icon.png" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    </head>
    <body>
        <container id="container">
            <div class="profile_picture"><img title="profile picture" src="image/profile_picture.jpg"></div>
            <div class="name"><span>{name}</span></div>
            <div class="location"><i class="fas fa-map-marker-alt"></i> <span>{locashion}</span></div>
            <div class="discription"><span>{discription}<i class="fas fa-laptop-code" style="font-size:12px;"></i></span></div><hr>
            <div class="social-media">
                <a href="https://instagram.com/{instagram}" target="_blank" style="top: -100px;transition-duration:0.3s;">
                    <div class="instagram">
                        <i class="fab fa-instagram" style="background:none;font-size:25px;"></i> INSTAGRAM
                    </div>
                </a>
                <a href="https://www.snapchat.com/add/{snapchat}" target="_blank" style="top: -100px;transition-duration:0.5s;">
                    <div class="snapchat">
                        <i class="fab fa-snapchat" style="background:none;font-size:25px;"></i> SNAPCHAT
                    </div>
                </a>
                
                <a href="https://t.me/{telegram}" target="_blank" style="top: -100px;transition-duration:0.7s;"> 
                    <div class="telegram">
                        <i class="fab fa-telegram" style="background:none;font-size:25px;"></i> TELEGRAM
                    </div>
                </a>
                <a href="https://twitter.com/{twitter}" target="_blank" style="top: -100px;transition-duration:0.9s;"> 
                    <div class="twitter">
                        <i class="fab fa-twitter" style="background:none;font-size:25px;"></i> TWITTER
                    </div>
                </a>
            </div>
            <div class="footer">Powered by <a href="https://t.me/CodeLeak" target="_blank">APIS.RED</a></div>
        </container>
        <script src="js/main.js?Cash=232342"></script>
    </body>
    </html>
    '''

    with open('../public_html/pages/'+the_ran_name,'w') as the_bin_file:
        the_bin_file.writelines(data)

    data = {'stats':'Done','url':f'https://apis.red/pages/{the_ran_name}'}
    json_string = json.dumps(data, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response

if __name__ == '__main__':
    app.run()
