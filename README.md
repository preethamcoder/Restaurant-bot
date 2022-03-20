# Cento-Restaurant-bot

This is a bot that can do many things, including:
1. Greet users
2. Show menu
3. Show offers available
4. Display vegetarian options
5. Display vegan options
6. Explain more about any particular item, preparation, and its ingredients
7. Show Restaurant's COVID policies
8. Check available tables
9. Book tables, and give unique ID
10. Answer if asked about identity
11. Take positive and negative feedback and respond accordingly
12. Respond to general messages
13. Bid the user goodbye

Technologies used: **Python, NLP, Flask, HTML, CSS, JS, and MongoDB**

# How to use?

1. First, download fasttext from `https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz`.
2. Next, clone this repo.
3. Move the zip file in step one to the location of the cloned repo and change your directory.
4. Run `prepare_ft_model.py` from the helpers folders and extract this file.
5. Now, run `data_embeddeder.py` to prepare data.
6. Create a `.env` file and create a variable called `database1`. Add your mongodb connection key to that.
7. Then, run app.py and open the resultant link.
8. Enjoy! 
