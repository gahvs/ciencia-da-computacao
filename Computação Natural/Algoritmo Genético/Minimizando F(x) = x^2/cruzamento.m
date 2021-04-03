function POPnovo = cruzamento(POP,xmin,xmax,metCRUZ)
    % Apenas para auxílio, caso necessário
    [tamPOP, numVAR] = size(POP);

    switch metCRUZ
        case 1 % média
            POPnovo = (xmin + xmax) / 2;
        case 2 % valor aleatório entre x1 e x2
            POPnovo = xmin + (rand * (xmax - xmin));
        case 3 % valor aleatório que extrapola o intervalo entre x1 e x2
            POPnovo = xmin + (2 * rand - .5) * (xmax - xmin);
        otherwise
            fprintf('MÉTODO DE CRUZAMENTO NÃO IMPLEMENTADO');
    end
    
    % Para garantir que a nova população não extrapole o espaco de busca
    POPnovo = max(POPnovo,xmin);
    POPnovo = min(POPnovo,xmax);
end