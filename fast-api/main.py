from fastapi import FastAPI
import random

app = FastAPI()


slide_hustle = [
"Freelancing - Start offering your skills online!",
"Dropshipping - Sell without handling inventory!",
"Stock Market - Invest and watch your money grow!",
"Affiliate Marketing - Earn by promoting products!",
"Crypto Trading - Buy and sell digital assets!",
"Online Courses - Share your knowledge and earn!",
"Print-on-Demand - Sell custom-designed products!",
"Blogging - Create content and earn through ads and sponsorships!",
"YouTube Channel - Monetize videos through ads and sponsorships!",
"Social Media Management - Manage accounts for brands and influencers!",
"App Development - Create mobile or web applications for businesses!"
]

many_quotes = [
"The only way to do great work is to love what you do. - Steve Jobs", 
"Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
"If you don’t find a way to make money while you sleep, you will work until you die. - I",
"The best way to predict the future is to invent it. - Alan Kay",
"Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
"The only way to do great work is to love what you do. - Steve Jobs",
"Money is a terrible master but an excellent servant. - P.T. Barnum",
"You must gain control over your money or the lack of it will forever control you. - Dave Ramsey",
"Opportunities don’t happen. You create them. - Chris Grosser",
"Don’t stay in bed unless you can make money in bed. - George Burns",
"Money often costs too much. - Ralph Waldo Emerson",
"Never depend on a single income. Make an investment to create a second source. - Warren Buffett",
"The way to get started is to quit talking and begin doing. - Walt Disney",
"It’s not about having lots of money. It’s about knowing how to manage it. - Anonymous",
"Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. - Anonymous",
"Being rich is having money; being wealthy is having time. - Margaret Bonnano",
"A wise person should have money in their head, but not in their heart. - Jonathan Swift",
"Money grows on the tree of persistence. - Japanese Proverb",
"The best way to predict the future is to invent it. - Alan Kay",
"The only way to do great work is to love what you do. - Steve Jobs",
"The way to get started is to quit talking and begin doing. - Walt Disney",
"Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
"If you don’t find a way to make money while you sleep, you will work until you die. - I",
"Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
"Money is a terrible master but an excellent servant. - P.T. Barnum",
"You must gain control over your money or the lack of it will forever control you. - Dave Ramsey",
"Opportunities don’t happen. You create them. - Chris Grosser",
"Don’t stay in bed unless you can make money in bed. - George Burns",
"Money often costs too much. - Ralph Waldo Emerson",
"Never depend on a single income. Make an investment to create a second source. - Warren Buffett",
"It’s not about having lots of money. It’s about knowing how to manage it. - Anonymous",
"Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. - Anonymous",
"Being rich is having money; being wealthy is having time. - Margaret Bonnano",
"A wise person should have money in their head, but not in their heart. - Jonathan Swift",
"Money grows on the tree of persistence. - Japanese Proverb",
]




@app.get("/slide_hustle")
def get_slide_hustles():
    """" Return a random slide hustle idea """
    # if api_key != "1234567890":
    # return {"error": "Invalid API key"}
    return {
        "hustle": random.choice(slide_hustle)
    }




@app.get("/money_quotes")
def get_money_quotes(api_key: str):
    """" Return a random money quote """
    if api_key != "1234567890":
        return {"error": "Invalid API key"}
    return {
        "money_quote": random.choice(many_quotes)
    }
