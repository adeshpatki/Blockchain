import fastapi as _fastapi
import blockchain as _blockchain


blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()

#mining
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, details="The Blockchain is invaild"
        )
    block = blockchain.mine_block(data=data)

    return block

#get entire chain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, details="The Blockchain is invaild"
        )

    chain = blockchain.chain
    return chain       


#return the last block
@app.get("/blockchain/last/")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
        
    return blockchain.get_previous_block()    

#validation
@app.get("/validate/")
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.is_chain_valid()





