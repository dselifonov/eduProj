const
    path = require('path'),
    webpack = require('webpack');

module.exports = {
    entry: {
        commons: "./apps/commons/static/js/index.js",
        cabinet: "./apps/cabinet/static/js/index.js",
    }
    ,
    output: {
        path: path.resolve(__dirname, './compiled_static'),
        filename:
            "[name].js"
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)/,
                exclude: /node_modules/,
                use: "babel-loader"
            },
            {
                test: /\.svg$/,
                loader: "file-loader"
            },
            {
                test: /\.(eot|svg|png|ttf|woff|woff2)$/,
                loader: "file-loader",
                options: {
                    name: 'fonts/[name].[ext]'
                }
            }
        ]
    }
    ,
    resolve: {
        extensions: ['.js', '.jsx']
    }
    ,
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendor',
            minChunks: 2
        })
    ]
};