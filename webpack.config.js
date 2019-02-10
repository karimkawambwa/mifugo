module.exports = {
    watchOptions: {
        ignored: /node_modules/
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        },
        {
            test: /\.css?$/,
            use: [{
                loader: "css-loader",
                options: {

                    importLoaders: 1
                }
            }]
        }
      ]
    }
  };