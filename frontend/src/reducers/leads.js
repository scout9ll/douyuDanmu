import { GET_LEADS } from "../actions/types.js";

const initialState = {
  lead: []
};
export default function(state = initialState, action) {
  switch (action.type) {
    case GET_LEADS:
      return {
        ...state,
        lead: action.payload
      };
    default:
      return state;
  }
}
