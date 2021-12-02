FROM node:16 as builder
WORKDIR /cloud
COPY . ./
RUN rm -rf /cloud/dist
RUN npm run build:prod

FROM nginx:latest
COPY --from=builder /cloud/dist/* /usr/share/nginx/html/
COPY --from=builder /cloud/dist/static /usr/share/nginx/html/static
COPY nginx /etc/nginx/
RUN ls /usr/share/nginx/html/
CMD ["nginx","-g","daemon off;"]
#CMD ["npm","run","dev"]
