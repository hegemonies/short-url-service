FROM node:20-alpine as build
WORKDIR /app
COPY ./ .
RUN npm i
RUN npm run build || true

FROM nginx:1-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
