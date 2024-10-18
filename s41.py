import pandas as pd
data=pd.read_excel("houses.xlsx")
x=data[["meterage","rooms","floor","year","region"]]
y=data["price"]


from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)


new_data = pd.DataFrame([[70, 1, 2, 17, 2]], columns=["meterage",
"rooms", "floor", "year", "region"])
ypred = model.predict(new_data)

print("ypred = ",ypred)
