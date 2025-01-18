from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_users():
    bigjoe = User(
        username="bigjoe", email='edgelord420@zune.net', password='password69', bio='Founder. Innovator. I made this website for real for real.', profile_pic='', profile_banner=''
    )
    johnpork = User(
        username="johnpork", email="johnpork@zune.net", password="johnpeniz420", bio="Based in London, also based. It's me, John Pork!", profile_pic='https://bandfishbucket.s3.us-east-1.amazonaws.com/f2790fae96e94414b0739373e6ddbbfe.jpg', profile_banner=''
    )
    bk4prez = User(
        username="benkissel1", email="sidestorieslpotl@zune.net", password="bk4brooklynPrez", bio="1/3 Owner of LPN. Host of OKBud! Last Podcast just isn't as funny without me.", profile_pic="", profile_banner=""
    )
    jackalope = User(
    username="jackalopeJump", email="jumpjackalope@zune.net", password="H0rnb0iz", bio="Hopping through life with style. Meme collector and cryptid enthusiast.", profile_pic="https://example.com/jackalope_profile.jpg", profile_banner="https://example.com/jackalope_banner.jpg"
    )
    tofuWrestler = User(
    username="tofuWrestler99", email="tofu.king@zune.net", password="Soy4Life123", bio="Plant-based pro wrestler. Breaking hearts and stereotypes, one suplex at a time.", profile_pic="https://example.com/tofu_profile.jpg", profile_banner="https://example.com/tofu_banner.jpg"
    )
    spaghettiWizard = User(
    username="spaghettiWizard", email="noodlemagic@zune.net", password="AbracaSpaghett", bio="Casting spells and eating shells. DM me your pasta puns.", profile_pic="https://example.com/spaghetti_profile.jpg", profile_banner="https://example.com/spaghetti_banner.jpg"
    )
    quantumSloth = User(
    username="quantumSloth", email="slowtime@zune.net", password="Schrod1ng3r", bio="Simultaneously lazy and productive. Ask me about black holes or naps.", profile_pic="https://example.com/sloth_profile.jpg", profile_banner=""
    )

    pebbleHunter = User(
    username="pebbleHunter", email="pebblesforlife@zune.net", password="St0neS33ker", bio="Geologist on a quest for the world's most beautiful rocks. Rock on!", profile_pic="", profile_banner="https://example.com/pebble_banner.jpg"
    )

    db.session.add(bigjoe)
    db.session.add(johnpork)
    db.session.commit()

def undo_users():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
