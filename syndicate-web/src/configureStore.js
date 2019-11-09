import { createBrowserHistory } from "history";
import { apiMiddleware } from "redux-api-middleware";
import { applyMiddleware, createStore } from "redux";

import { persistReducer, persistStore } from "redux-persist";
import storage from "redux-persist/es/storage";
import { createFilter } from "redux-persist-transform-filter";

import { routerMiddleware } from "connected-react-router";
import createRootReducer from "./reducers";

export const history = createBrowserHistory();

export default function configureStore(preloadedState) {
  const persistedFilter = createFilter("auth", ["access", "refresh"]);

  const reducer = persistReducer(
    {
      key: "polls",
      storage: storage,
      whitelist: ["auth"],
      transforms: [persistedFilter]
    },
    createRootReducer(history)
  );

  const store = createStore(
    reducer,
      {},
    applyMiddleware(apiMiddleware, routerMiddleware(history))
  );

  persistStore(store);
  return store;
}
